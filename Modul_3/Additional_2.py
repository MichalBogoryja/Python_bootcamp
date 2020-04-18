<<<<<<< HEAD
from typing import Union
def build_bridge(small: int, big: int, goal: int) -> Union[str, bool]:
=======

def build_bridge(small: int, big: int, goal: int):
>>>>>>> 887490dd471f73192f15a2e01b43d8772e671b21
    # goal - odległość do wypełnienia
    # small - długość mniejszej płyty
    # big - długość większej płyty
    # return True # Zwróć wartość True jeśli można zbudować most
                #lub False jeśli nie możemy go zbudować
    result_s: int = 0
    result_b: int = 0
    possible = False

    check_s = goal % small
    check_b = goal % big

    if check_s == 0:
        result_s = int(10 / 5)
        possible = True
    if check_b == 0:
        result_b = int(goal / big)
        possible = True

    if check_s != 0 and check_b != 0:
        occurrence_number_s = (goal - check_s) / small
        occurrence_number_b = (goal - check_b) / big

        for i in range(int(occurrence_number_s)):
            new_goal = goal - i*small
            check_s_b = new_goal % big
            if check_s_b == 0:
                result_s = i
                result_b = int(new_goal / big)
                possible = True
                break

    if possible:
        print(f"[small: {small}, big: {big}, goal: {goal}] Dla mostu o długości {goal}, potrzeba: {result_s} małych ({small}) fragmentów i {result_b} dużych ({big}).")
        return True
    else:
        print(f"[small: {small}, big: {big}, goal: {goal}] Nie da się zbudować")
        return False


build_bridge(2, 5, 37)
build_bridge(3, 5, 37)
build_bridge(3, 36, 37)
