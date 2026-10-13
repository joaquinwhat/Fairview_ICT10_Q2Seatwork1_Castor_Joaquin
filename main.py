from pyscript import document

club_members = ["Phoenix Hizon", "Nathan Ladion", "Erin Urbano", "James Diaz", "Jericho Magsalin", "Louie Lee"]

def check_club(e):
    first_name = document.getElementById("firstName").value
    last_name = document.getElementById("lastName").value

    full_name = first_name + " " + last_name

    result = document.getElementById("result")

    result.innerText = "Sorry " + full_name + ", your name is not on the list."