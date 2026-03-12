#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import speech_recognition as sr
import pyttsx3
import nltk
from datetime import datetime
from ai_response import get_ai_response
from voice_input import VoiceInputHandler

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Initialize speech recognizer
recognizer = sr.Recognizer()

class SanuAIChatbot:
    def __init__(self):
        self.name = "Sanu AI"
        self.conversation_history = []
        self.is_running = True
        self.voice_handler = VoiceInputHandler()
        
    def speak(self, text):
        """Convert text to speech"""
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"[ERROR] Voice output failed: {e}")
    
    def listen(self):
        """Listen to user voice input"""
        try:
            text = self.voice_handler.listen()
            return text.lower() if text else None
        except Exception as e:
            print(f"[ERROR] Listening failed: {e}")
            return None
    
    def get_response(self, user_input):
        """Generate AI response"""
        try:
            response = get_ai_response(user_input)
            return response
        except Exception as e:
            return f"I encountered an error: {str(e)}"
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print(f"🤖 {self.name} Chatbot - Main Menu")
        print("="*50)
        print("1. [T] Type message")
        print("2. [V] Voice message")
        print("3. [H] Chat history")
        print("4. [Q] Quit")
        print("="*50)
        print("Enter choice (T/V/H/Q): ", end="")
    
    def show_history(self):
        """Display conversation history"""
        if not self.conversation_history:
            print("\n[INFO] No conversation history yet.\n")
            return
        print("\n" + "="*50)
        print("📝 Conversation History")
        print("="*50)
        for i, (user, bot) in enumerate(self.conversation_history, 1):
            print(f"\n[{i}] YOU: {user}")
            print(f"    {self.name}: {bot}")
        print("\n" + "="*50 + "\n")
    
    def chat_text(self):
        """Text-based chat"""
        print(f"\n[{self.name}] Type your message (or 'back' to return):")
        user_input = input("[YOU] ").strip()
        if user_input.lower() == 'back':
            return
        if not user_input:
            print(f"[{self.name}] Please enter a message.\n")
            return
        response = self.get_response(user_input)
        print(f"[{self.name}] {response}\n")
        self.conversation_history.append((user_input, response))
    
    def chat_voice(self):
        """Voice-based chat"""
        print(f"\n[{self.name}] Speak your message now...")
        user_input = self.listen()
        if not user_input:
            return
        response = self.get_response(user_input)
        print(f"[{self.name}] {response}")
        self.speak(response)
        self.conversation_history.append((user_input, response))
    
    def run(self):
        """Main chatbot loop"""
        print("\n" + "="*50)
        print(f"🎉 Welcome to {self.name}!")
        print("📱 Running on Termux")
        print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50)
        while self.is_running:
            try:
                self.display_menu()
                choice = input().strip().upper()
                if choice == 'T':
                    self.chat_text()
                elif choice == 'V':
                    self.chat_voice()
                elif choice == 'H':
                    self.show_history()
                elif choice == 'Q':
                    print(f"\n[{self.name}] Thank you for chatting with me! Goodbye! 👋\n")
                    self.speak("Thank you for chatting with me. Goodbye!")
                    self.is_running = False
                else:
                    print(f"[{self.name}] Invalid choice. Please try again.\n")
            except KeyboardInterrupt:
                print(f"\n\n[{self.name}] Chatbot interrupted. Goodbye! 👋\n")
                self.is_running = False
            except Exception as e:
                print(f"[ERROR] {str(e)}\n")

def main():
    """Start the chatbot"""
    chatbot = SanuAIChatbot()
    chatbot.run()

if __name__ == '__main__':
    main()