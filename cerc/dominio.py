
def get_register_key(path, cpf_cnpj):
    list = set()
    with open(path, "r") as file:
        for f in file:
            item = f.strip()
            list.add(item[91:108]) if item[3:17] == cpf_cnpj else None
        for x in list:
            print(x)


if __name__ == "__main__":
    get_register_key("C:\\Users\\lucas.abreu\\Desktop\\CERC-A001T006-02_22347623_20200210_00001.dom", "22455826000188")