from pyscript import document

club_members = ["John Hizon", "Mark Ladion", "Paul Urbano", "James Diaz", "Carlos Magsalin", "Daniel Lee"]

def check_club(e):
    first_name = document.getElementById("firstName").value
    last_name = document.getElementById("lastName").value

    full_name = first_name + " " + last_name

    result = document.getElementById("result")

    result.innerText = "Sorry " + full_name + ", your name is not on the list."