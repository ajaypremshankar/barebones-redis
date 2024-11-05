def encode_resp(raw_resp=None, resp_type=None):
    if not resp_type:
        return f"+{raw_resp}\r\n".encode()
    elif resp_type == 'bulk_string':
        return f"${len(raw_resp)}\r\n{raw_resp}\r\n".encode()
    elif resp_type == 'null':
        return f"$-1\r\n".encode()
    elif resp_type == 'array_bulk_string':
        resp = f"*{len(raw_resp)}\r\n"
        for rr in raw_resp:
            resp += f"${len(rr)}\r\n{rr}\r\n"
        return resp.encode()
