from datetime import date


class DataValidationError(Exception):
    ...


class TeamValidator:
    valid_keys = [
        "name",
        "titles",
        "top_scorer",
        "fifa_code",
        "founded_at",
    ]

    valid_inputs = {
        "name": str,
        "titles": int,
        "top_scorer": str,
        "fifa_code": str,
        "founded_at": date,
    }

    def __init__(self, *args: tuple, **kwargs: dict):
        self.data = kwargs
        self.errors = {}

    def is_valid(self) -> bool:
        """
        1. limpar dados
            (clean_data)
        2. Verificar se todas as chaves obrigatorias foram passadas
        3.
        """

        # 1. Limpeza de chaves extras
        self.clean_data()
        try:
            # 2. Verificação de chaves obrigatorias
            self.validate_required_keys()
            self.validate_data_types()

            return True
        except (KeyError, DataValidationError):
            return False

    def clean_data(self):
        data_keys = list(self.data.keys())

        for key in data_keys:
            if key not in self.valid_keys:
                self.data.pop(key)

    def validate_required_keys(self):
        for valid_key in self.valid_keys:
            if valid_key not in self.data.keys():
                self.errors[valid_key] = "missing key"
                # self.errors.update({valid_key: "missing key"})

        # TRUTY OF FALSY VALUES
        # self.errors = {} -> Falso
        # self.errors = {'name': "missing key"} -> True
        if self.errors:
            raise KeyError

    def validate_data_types(self):
        # print()
        # print("VALIDATE DATA TYPES:")
        for valid_key, expected_type in self.valid_inputs.items():
            # print(valid_key, expected_type)
            # print("VALOR A SER VALIDADO", self.data[valid_key])
            # print("TIPO A SER VALIDADO", type(self.data[valid_key]))
            # print("TIPO ESPERADO", expected_type)
            if type(self.data[valid_key]) is not expected_type:
                # err_msg = "wrong value"
                # err_msg = f"expected `{valid_key}` to be an {expected_type}"
                err_msg = f"must be a {expected_type.__name__}"
                self.errors[valid_key] = err_msg

        if self.errors:
            # raise KeyError
            raise 