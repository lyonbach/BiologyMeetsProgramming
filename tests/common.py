import ast

def clean_line(line: str) -> str:

    return line.replace('\n', '').lstrip().rstrip().replace('"', "'")

def interpret_line(line: str) -> type:

    if line.startswith('{') or line.startswith('['):
        return ast.literal_eval(line)
    else:
        return line

def retrieve_test_data(file_path: str, output_as_list: bool=False) -> tuple:

    with open(file_path, 'r') as stream:

        record_input, record_output = False, False
        test_data, input_data = [], []
        output_data = [] if output_as_list else None

        for line in stream.readlines():
            if line.startswith("Input"):
                record_input = True
                record_output = False
                continue
            elif line.startswith("Output"):
                record_input = False
                record_output = True
                continue
            elif line.startswith("Test"):
                if input_data and output_data:
                    test_data.append((input_data, output_data))
                    input_data = []
                    output_data = [] if output_as_list else None
                continue
            if record_input:
                line = interpret_line(clean_line(line))
                if not line:
                    continue
                input_data.append(line)
            elif record_output:
                line = interpret_line(clean_line(line))
                if not line:
                    continue
                if output_as_list:
                    output_data.append(line)
                else:
                    output_data = line

        test_data.append((input_data, output_data))

    return test_data
