from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from .models import Team
from django import forms
from django.contrib import messages
from .models import Round2Submission

def index(request):
    # Fetch all posts from the database
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def landing_page(request):
    if request.method == 'POST':
        # Get the form data
        team_name = request.POST.get('team_name')
        team_members = request.POST.get('team_members')
        contact_email = request.POST.get('contact_email')
        
        # Create a new team object and save it to the database
        team = Team.objects.create(name=team_name, members=team_members, contact_email=contact_email)
        
        # Redirect to the registration success page or any other page you want to display
        return redirect('round1')

    return render(request, 'landing_page.html')

def round1(request):
    questions = [
        {'id': 1, 'question': "I am taken from a mine and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?", 'answer': 'Pencil', 'correct': None},
        {'id': 2, 'question': "I have keys but open no locks. I have space but have no room. You can enter, but you can't go outside. What am I?", 'answer': 'Keyboard', 'correct': None},
        {'id': 3, 'question': "The more you take, the more you leave behind. What am I?", 'answer': 'Footsteps', 'correct': None},
        {'id': 4, 'question': "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", 'answer': 'Echo', 'correct': None},
        {'id': 5, 'question': "I am full of holes, yet I can hold water. What am I?", 'answer': 'Sponge', 'correct': None},
    ]

    if request.method == 'POST':
        for question in questions:
            user_answer = request.POST.get(f'answer_{question["id"]}')
            if user_answer.lower() == question['answer'].lower():
                question['correct'] = True
            else:
                question['correct'] = False

        all_correct = all(question['correct'] for question in questions)
        if all_correct:
            return render(request, 'round1_success.html')

    return render(request, 'round1.html', {'questions': questions})

def round1_success(request):
    # Process the form submission and handle the code entered by participants
    if request.method == 'POST':
        volunteer_code = request.POST.get('volunteer_code')
        
        # Check if the entered code matches the volunteer code
        if volunteer_code == 'VIT@FU':
            # If the code is correct, redirect participants to Round 2 page
            return redirect('round2')
        else:
            # If the code is incorrect, show an error message or redirect back to Round 1 with an error flag
            return render(request, 'round1_success.html', {'error_message': 'Incorrect code entered. Please try again.'})

    # If it's a GET request or no valid code is entered, display the Round 1 success page again
    return render(request, 'round1_success.html')

def round2(request):
    challenges = [
        {
            'id': 1,
            'title': 'Challenge 1',
            'description': 'Description of Challenge 1',
            'ciphered_text': 'ciphered_text_for_challenge_1',
            'shift_key': 3,
            'solution': 'solution_for_challenge_1',
        },
        {
            'id': 2,
            'title': 'Challenge 2',
            'description': 'Description of Challenge 2',
            'ciphered_text': 'ciphered_text_for_challenge_2',
            'shift_key': 2,
            'solution': 'solution_for_challenge_2',
        },
        # Add more challenges as needed
    ]

    if request.method == 'POST':
        # Handle form submission and check answers
        for challenge in challenges:
            challenge_id = str(challenge['id'])
            user_answer = request.POST.get(f'answer_{challenge_id}')
            if user_answer.lower() == challenge['solution'].lower():
                challenge['correct'] = True
            else:
                challenge['correct'] = False

        # After processing the answers, if all answers are correct, move on to Round 3
        if all(challenge['correct'] for challenge in challenges):
            return redirect('round3')

    return render(request, 'round2.html', {'challenges': challenges})


def create_sample_maze():
    return [
        ['#', '#', '#', '#', '#', '#'],
        ['#', 'S', ' ', ' ', '#', '#'],
        ['#', '#', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '#', '#'],
        ['#', ' ', ' ', ' ', '#', 'E'],
        ['#', '#', '#', '#', '#', '#'],
    ]

def dfs_solve_maze(maze, row, col):
    if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]) or maze[row][col] in ["#", "X"]:
        return False

    if maze[row][col] == "E":
        return True

    maze[row][col] = "X"
    return (
        dfs_solve_maze(maze, row - 1, col) or
        dfs_solve_maze(maze, row + 1, col) or
        dfs_solve_maze(maze, row, col - 1) or
        dfs_solve_maze(maze, row, col + 1)
    )


def round3(request):
    # Fetch all Round2Submission objects from the database
    submissions = Round2Submission.objects.all()

    # Pass the submissions data to the template for rendering
    return render(request, 'round3.html', {'submissions': submissions})


def submit_solution(request):
    if request.method == 'POST':
        # Get the form data
        participant_code = request.POST.get('participant_code')
        team_name = request.POST.get('team_name')

        # Ensure that 'team_name' is not empty
        if not team_name:
            return render(request, 'round3.html', {'error_message': 'Please provide a team name.'})

        # Save the submission in the Round2Submission model
        Round2Submission.objects.create(team_name=team_name, participant_code=participant_code)

        # Pass the team information to the pending page
        return render(request, 'round3_pending.html', {'team_name': team_name, 'participant_code': participant_code})

    # If it's a GET request or no code is submitted, display the Round 2 page again
    return render(request, 'round3.html')
