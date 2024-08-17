import datastruct4py as ds

def main():
    base_type = [
        ds.from_data_value('-1.2'),
        ds.from_data_value('"hello"'),
        ds.from_data_value('true'),
    ]

    assert base_type[0] == -1.2, f"Expected -1.2, got {base_type[0]}"
    assert base_type[1] == "hello", f"Expected 'hello', got {base_type[1]}"
    assert base_type[2] == True, f"Expected True, got {base_type[2]}"

    tuple_val = ds.from_data_value('(10, 20)')
    assert tuple_val == (10, 20), f"Expected (10, 20), got {tuple_val}"

    list_val = ds.from_data_value('[1.20, "hello", true, (10,20)]')
    assert list_val == [1.20, "hello", True, (10, 20)], f"Expected [1.20, 'hello', True, (10, 20)], got {list_val}"

    print("All tests passed!")

if __name__ == "__main__":
    main()












# import import datastruct4py as ds

# def main():

#     baseType = [
#         ds.from_data_value('-1.2'),
#         ds.from_data_value('"hello"'),
#         ds.from_data_value('true'),
#     ]

#     assert(baseType[0] == -1.2 and baseType[1] == "hello" and baseType[2] == True)

#     tuple  = ds.from_data_value('(10, 20)')
#     assert tuple == (10, 20)

#     list  = ds.from_data_value('[1.20 , "hello" , true , (10,20)]')
#     assert list == [1.20, "hello", true, (10, 20)] 

#     print("pass")


#     if __name__ == "__main__":
#         main()