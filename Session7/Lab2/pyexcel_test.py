import pyexcel

data  = [
    {
        "Name":"Huyền",
        "Age":20
    },
    {
        "Name":"Nam",
        "Age":24
    },
    {
        "Name":"Khánh",
        "Age":28
    },
    {
        "Name":"Yến",
        "Age":29
    },
]

pyexcel.save_as(records=data, dest_file_name = "test.xlsx")