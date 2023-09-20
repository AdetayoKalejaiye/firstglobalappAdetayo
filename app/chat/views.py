
# Create your views here.
from django.shortcuts import render, redirect
from .models import Group, Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Max
@login_required
def home(request):
    user = request.user
    
    # Retrieve groups where the user is a member
    groups = Group.objects.filter(members=user)
    search_query = request.GET.get('q')

    # Filter users based on the search query (if provided)
    if search_query:
        users = User.objects.filter(username__icontains=search_query)
        groups = groups.filter(name__icontains=search_query)
    else:
        users = User.objects.exclude(id=user.id)
    return render(request, 'chathome.html', { 'groups': groups, 'users': users, 'user': user})

@login_required
def user_chat(request, receiver_id):
    sender = request.user
    receiver = User.objects.get(pk=receiver_id)
    messages = Message.objects.filter(sender=sender, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=sender)
    messages = messages.order_by('timestamp')
    user = request.user
    
    # Retrieve groups where the user is a member
    groups = Group.objects.filter(members=user)
    search_query = request.GET.get('q')

    # Filter users based on the search query (if provided)
    if search_query:
        users = User.objects.filter(username__icontains=search_query)
        groups = groups.filter(name__icontains=search_query)
    else:
        users = User.objects.exclude(id=user.id)

    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(sender=sender, receiver=receiver, content=content)

    return render(request, 'user_chat.html', {'receiver': receiver, 'messages': messages, 'users': users, 'user': user, 'groups':groups})

@login_required
def create_user_chat(request,receiver_id):
    receiver = User.objects.get(pk=receiver_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return redirect('user_chat', receiver_id=receiver_id)
    
    users = User.objects.all().exclude(id=request.user.id)
    return render(request, 'create_user_chat.html', {'receiver': receiver, 'users': users})

@login_required
def group_chat(request, group_id):
    group = Group.objects.get(pk=group_id)
   
    messages = Message.objects.filter(group=group).order_by('timestamp')
    user = request.user
    
    # Retrieve groups where the user is a member
    groups = Group.objects.filter(members=user)

    search_query = request.GET.get('q')
    events = group.event_set.all()
  


   #Combine the events and messages for a group
    message_and_event_list = [*messages, *events]

   # Sort the combination by the timestamp so that they are listed in order
    sorted_message_event_list = sorted(message_and_event_list, key=lambda x :     x.timestamp)

   #get the list of all group members
    group_members = group.members.all()
    # Filter users based on the search query (if provided)
    if search_query:
        users = User.objects.filter(username__icontains=search_query)
    else:
        users = User.objects.exclude(id=user.id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(group=group, sender=request.user, content=content)

    return render(request, 'group_chat.html', {'group': group, 'messages': messages, 'groups': groups, 'users': users, 'user': user, 'events':events, "message_and_event_list":sorted_message_event_list, "group_members":group_members,})

@login_required
def create_group_chat(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        member_ids = request.POST.getlist('members')
        
        # Create a new group with the specified name
        group = Group.objects.create(name=group_name)
        
        # Add members to the group
        group.members.set(member_ids)
        
        # Redirect to the group chat page with the group's ID in the URL
        return redirect('group_chat', group_id=group.id)
    
    users = User.objects.all()
    return render(request, 'create_group_chat.html', {'users': users})
