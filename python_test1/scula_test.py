
# (['234-567-890', '444-444-444', '321-543-234'], ['Harry', 'Nick', 'Michael'], '444-444-444')


def solution(phone_numbers, phone_owners, number):
    # write your code in Python 3.6
    try:
        pos = phone_numbers.index(number)
        return phone_owners[pos]

    except ValueError:
        return number


print(solution(['234-567-890', '444-444-444', '321-543-234'], ['Harry', 'Nick', 'Michael'], '444-444-444'))


def decks(A, B):
    letter_dic = {'T': 100, 'J': 101, 'Q': 102, 'K': 103, 'A': 104}
    result = 0

    for pos in range(len(A)):
        value_A, value_B = 0, 0

        value_A = int(A[pos]) if A[pos].isnumeric() else letter_dic[A[pos]]  
        value_B = int(B[pos]) if B[pos].isnumeric() else letter_dic[B[pos]] 

        if value_A > value_B:
            result += 1

    return result


print(decks('A586QK', 'JJ653K'))
print(decks('23A84Q', 'K2Q25J'))

'''
select tasks.id as task_id, tasks.name as task_name, 
CASE
    WHEN avg(reports.score)<=20 THEN 'Hard'
    WHEN avg(reports.score)<=60 THEN 'Medium'
	ELSE 'Easy'
  END 
 as average
from tasks INNER join reports on reports.task_id = tasks.id
GROUP by tasks.id, tasks.name
order by tasks.id;


'''
