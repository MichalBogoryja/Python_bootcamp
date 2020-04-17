
def build_bridge(small, big, goal):
    # goal - odległość do wypełnienia
    # small - długość mniejszej płyty
    # big - długość większej płyty
    # return True # Zwróć wartość True jeśli można zbudować most
                #lub False jeśli nie możemy go zbudować
    result_s = 0
    result_b = 0
    possible = False

    check_s = goal % small
    check_b = goal % big

    if check_s == 0:
        result_s = goal / small
        possible = True
    if check_b == 0:
        result_b = goal / big
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