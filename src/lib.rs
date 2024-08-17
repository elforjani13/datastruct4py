use std::collections::HashMap;

use datastruct_rs::DValue;
use pyo3::prelude::*;

#[pyfunction]
fn from_data_value(py: Python, value: String) -> PyResult<PyObject> {
    let result = match DValue::from(&value) {
        DValue::None => py.None(),
        DValue::String(s) => s.into_py(py),
        DValue::Number(n) => n.into_py(py),
        DValue::Boolean(b) => b.into_py(py),
        DValue::List(l) => {
            let mut obj: Vec<PyObject> = vec![];

            for item in l {
                obj.push(from_data_value(py, item.to_string())?);
            }
            obj.into_py(py)
        }
        DValue::Dict(d) => {
            let mut obj: HashMap<String, PyObject> = HashMap::new();
            for (k, v) in d {
                obj.insert(k.clone(), from_data_value(py, v.to_string())?);
            }
            obj.into_py(py)
        }
        DValue::Tuple(t) => (
            from_data_value(py, t.0.to_string())?,
            from_data_value(py, t.1.to_string())?,
        )
            .into_py(py),
        DValue::BinaryUtil(b) => {
            let temp = b.read();
            temp.into_py(py)
        }
    };
    Ok(result)
}

#[pyfunction]
fn dump_data_value(object: PyObject) -> PyResult<String> {
    let val = object_to_value(object);
    Ok(String::from(val.to_string()))
}

fn object_to_value(object: PyObject) -> DValue {
    Python::with_gil(|py| {
        if let Ok(s) = object.extract::<String>(py) {
            DValue::String(s)
        } else if let Ok(b) = object.extract::<bool>(py) {
            DValue::Boolean(b)
        } else if let Ok(n) = object.extract::<f64>(py) {
            DValue::Number(n)
        } else if let Ok((a, b)) = object.extract::<(PyObject, PyObject)>(py) {
            DValue::Tuple((Box::new(object_to_value(a)), Box::new(object_to_value(b))))
        } else if let Ok(l) = object.extract::<Vec<PyObject>>(py) {
            DValue::List(l.into_iter().map(object_to_value).collect())
        } else if let Ok(d) = object.extract::<HashMap<String, PyObject>>(py) {
            DValue::Dict(
                d.into_iter()
                    .map(|(k, v)| (k, object_to_value(v)))
                    .collect(),
            )
        } else {
            DValue::None
        }
    })
}

#[pymodule]
fn datastruct4py(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(from_data_value, m)?)?;
    m.add_function(wrap_pyfunction!(dump_data_value, m)?)?;
    Ok(())
}
