def solution(address):
    at_index = address.rfind("@") 
    domain_part = address[at_index + 1:]
    return domain_part
