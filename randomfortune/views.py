from django.shortcuts import render
import random


fortuneList = [
   "welcome sarorsaad.",
   "hi mlaz.",
   "hi marwa.",
   "hi mohmd.",
  
]
def fortune(request):
    fortune = random.choice(fortuneList)
    context = {
    "fortune": fortune
    }
    return render (request, "randomfortune/fortune.html",context)