from importlib.resources import files

OP_ERASE = "erase"
OP_CHECK = "check"
ATF_1502 = "ATF1502"
ATF_1504 = "ATF1504"
ATF_1508 = "ATF1508"

STANDARD_VECTORS = {
    OP_ERASE: {
        ATF_1502: files("atfu.standard_vectors").joinpath("e1502.xsvf"),
        ATF_1504: files("atfu.standard_vectors").joinpath("e1504.xsvf"),
        ATF_1508: files("atfu.standard_vectors").joinpath("e1508.xsvf"),
    },
    OP_CHECK: {
        ATF_1502: files("atfu.standard_vectors").joinpath("bc1502.xsvf"),
        ATF_1504: files("atfu.standard_vectors").joinpath("bc1504.xsvf"),
        ATF_1508: files("atfu.standard_vectors").joinpath("bc1508.xsvf"),
    },
}


def find_vector_file(operation: str, device_key: str):
    return STANDARD_VECTORS.get(operation, {}).get(device_key)


def atf_device_key(number: int):
    match number:
        case 1502:
            return ATF_1502
        case 1504:
            return ATF_1504
        case 1508:
            return ATF_1508
        case _:
            raise ValueError(f"{number} is not valid supported ATF CPLD device")
