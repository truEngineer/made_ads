A_DIV = 2 ** 16
B_DIV = 2 ** 30
N_MAX = 10 ** 7
 
 
def sum_a_sequence_gen(a_term, a_lin, a_const, n_elems):
    sum_a = a_term  # array of sum
    yield sum_a  # yield sum[0]
    for ind in range(n_elems):
        # yield sum[ind + 1]
        a_term = (a_lin * a_term + a_const) % A_DIV
        sum_a += a_term
        yield sum_a
 
 
def requests_gen(requests_number, b_term, b_lin, b_const, divider):
    request = []
    request.append(b_term % divider)  # add c[0] to the first request
    for _ in range(2 * requests_number):
        b_term = (b_lin * b_term + b_const) % B_DIV  # b[i]
        c_term = b_term % divider  # c[i]
        request.append(c_term)
        if len(request) == 2:  # request is ready
            # yield request[ind % 2] = [left, right] 
            yield sorted(request)
            request.clear()
            
 
def rsq(left, right, sum_arr):
    if left == 0:
        return sum_arr[right]
    return sum_arr[right] - sum_arr[left - 1]
 
 
n, x, y, a_0 = map(int, input().split()) # read input data
sum_a = [sum_i for sum_i in sum_a_sequence_gen(a_0, x, y, n)]  # array of the sequence "a" sum's
m, z, t, b_0 = map(int, input().split())
requests_answers_sum = 0  # for answers sum
for left, right in requests_gen(m, b_0, z, t, n):  # requests
    requests_answers_sum += rsq(left, right, sum_a)
print(requests_answers_sum)
