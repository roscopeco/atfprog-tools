from importlib.resources import files

OP_ERASE = "erase"
OP_CHECK = "check"

# The "plain" variants are synonyms for AS
ATF_1502 = "ATF1502"
ATF_1504 = "ATF1504"
ATF_1508 = "ATF1508"

ATF_1502AS = "ATF1502AS"
ATF_1504AS = "ATF1504AS"
ATF_1508AS = "ATF1508AS"
ATF_1502ASV = "ATF1502ASV"
ATF_1504ASV = "ATF1504ASV"
ATF_1508ASV = "ATF1508ASV"

STANDARD_VECTORS = {
    OP_ERASE: {
        ATF_1502: files("atfu.standard_vectors").joinpath("e1502.xsvf"),
        ATF_1504: files("atfu.standard_vectors").joinpath("e1504.xsvf"),
        ATF_1508: files("atfu.standard_vectors").joinpath("e1508.xsvf"),
        ATF_1502AS: files("atfu.standard_vectors").joinpath("e1502.xsvf"),
        ATF_1504AS: files("atfu.standard_vectors").joinpath("e1504.xsvf"),
        ATF_1508AS: files("atfu.standard_vectors").joinpath("e1508.xsvf"),
        ATF_1502ASV: files("atfu.standard_vectors").joinpath("e1502v.xsvf"),
        ATF_1504ASV: files("atfu.standard_vectors").joinpath("e1504v.xsvf"),
        ATF_1508ASV: files("atfu.standard_vectors").joinpath("e1508v.xsvf"),
    },
    OP_CHECK: {
        ATF_1502: files("atfu.standard_vectors").joinpath("bc1502.xsvf"),
        ATF_1504: files("atfu.standard_vectors").joinpath("bc1504.xsvf"),
        ATF_1508: files("atfu.standard_vectors").joinpath("bc1508.xsvf"),
        ATF_1502AS: files("atfu.standard_vectors").joinpath("bc1502.xsvf"),
        ATF_1504AS: files("atfu.standard_vectors").joinpath("bc1504.xsvf"),
        ATF_1508AS: files("atfu.standard_vectors").joinpath("bc1508.xsvf"),
        ATF_1502ASV: files("atfu.standard_vectors").joinpath("bc1502v.xsvf"),
        ATF_1504ASV: files("atfu.standard_vectors").joinpath("bc1504v.xsvf"),
        ATF_1508ASV: files("atfu.standard_vectors").joinpath("bc1508v.xsvf"),
    },
}


def find_vector_file(operation: str, device_key: str):
    return STANDARD_VECTORS.get(operation, {}).get(device_key)
