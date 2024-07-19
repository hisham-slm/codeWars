def ips_between(start, end):
    first_bits = bit_seperater(start)
    second_bits = bit_seperater(end)
    total_value_of_ip1 = bit_multiplier(first_bits)
    total_value_of_ip2 = bit_multiplier(second_bits)
    return total_value_of_ip2 - total_value_of_ip1

def bit_multiplier(ip):   
    octet_values = {1 : 256**3, 2 : 256**2, 3 : 256, 4 : 1}
    result = 0
    for i, bit in enumerate(ip):
        result += octet_values[i+1] * bit[i+1]
    return result

def bit_seperater(ip):
    ip_bits = ip.split('.')
    splitted_ip = []
    for i, bit in enumerate(ip_bits):
        each_bit = dict({i+1 : int(bit)})
        splitted_ip.append(each_bit)
    return splitted_ip

print(ips_between('20.0.0.10', '20.0.1.0'))
