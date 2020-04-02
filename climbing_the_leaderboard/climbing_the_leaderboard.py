
# class climb:
#     def climbingLeaderboard(scores, alice):
#
#
#
#
#
# cl =climb()
# scores_count = int(input())
# scores = list(map(int, input().rstrip().split()))
# alice_count = int(input())
# alice = list(map(int, input().rstrip().split()))
# result =cl.climbingLeaderboard(scores, alice)



def rank(alice_score, scores):
    ranks = []
    rank = 1
    scorel = len(scores) - 1
    for position, score in enumerate(scores):
        if position == 0 and score <= alice_score:

            return rank

        if position <= 0:
            ranks.append((score, rank))
        else:
            prev_score = scores[position - 1]
            if prev_score == score:  # if prev element is same, keep the same rank
                ranks.append((score, rank))
            elif score <= alice_score:
                rank = rank + 1
                ranks.append((score, rank))
                print(f"score <= alice_score {score}")
                return rank
            elif scorel == position:
                rank = rank + 1
                if score > alice_score:
                    rank = rank + 1

                    return rank
            else:  # if prev element is higher, then increase the rank
                rank = rank + 1


def climb(alice_scores, scores):
    ranks = []
    for score in alice_scores:
        ranks.append(rank(score, scores))
    return ranks


def test_whatever_name():
    assert rank(5, [100, 100, 50, 40, 30, 10]) == 6
    assert rank(45, [100, 100, 50, 40, 30, 10]) == 3
    assert rank(101, [100, 100, 50, 40, 30, 10]) == 1
    assert rank(33, [100, 100, 50, 40, 30, 10]) == 4
    assert rank(0, [100, 100, 50, 40, 30, 10]) == 6

def test_climbing():
    assert climb([5,45,101,33,0],[100, 100, 50, 40, 30, 10]) == [6,3,1,4,6]

if __name__ == '__main__':
    scores = list(map(int,input().rstrip().split()))
    alice_scores = list(map(int,input().rstrip().split()))
    result = climb(alice_scores, scores)

    #rank = "\n".join(map(str,result))
    print(result)