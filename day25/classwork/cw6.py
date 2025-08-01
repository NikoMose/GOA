def grade_status(score):
    if score >= 90:
        print("შესანიშნავი")
    if score >= 60:
        if score < 90:
            print("დამაკმაყოფილებელი")
    if score < 60:
        print("ჩაჭრილია")
