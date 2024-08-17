import datastruct4py as ds

def main():
    base_type = [
        ds.dump_data_value("hello"),
        ds.dump_data_value(22.6),
        ds.dump_data_value(True),
    ]

    assert base_type[0] == '"hello"', f"Expected '\"hello\"', got {base_type[0]}"
    assert base_type[1] == "22.6", f"Expected '22.6', got {base_type[1]}"
    assert base_type[2] == "true", f"Expected 'true', got {base_type[2]}"

    tuple_val = ds.dump_data_value((1, "val"))
    assert tuple_val == "(1, 'val')", f"Expected (1, 'val'), got {tuple_val}"

    dict_val = ds.dump_data_value({"name": "val"})
    assert dict_val == '{"name": "val"}', f"Expected '{{\"name\": \"val\"}}', got {dict_val}"

    print("All tests passed!")

if __name__ == "__main__":
    main()











# import datastruct4py as ds

# def main():

#     baseType = [
#         ds.dump_data_value("hello"),
#         ds.dump_data_value(22.6),
#         ds.dump_data_value(True),
#     ]

#     assert(baseType[0] == '"hello"' and baseType[1] == "22.6" and baseType[2] == "True")

#     tuple  = ds.dump_data_value((1, "val"))
#     assert tuple == "(1, 'val')"

#     dict = ds.dump_data_value({
#         "name": "val",
#     })
#     assert dict == '{"name": "val"}'

#     print("pass")


#     if __name__ == "__main__":
#         main()


