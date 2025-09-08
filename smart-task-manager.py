#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm, IntPrompt
from rich import box
from rich.text import Text
from rich.layout import Layout
import pyfiglet

console = Console()

class SmartTaskManager:
    def __init__(self):
        self.data_file = Path("todo_data.json")
        self.tasks = self.load_data()
        self.categories = ["Work", "Personal", "Study", "Shopping", "Health"]
        self.priorities = ["High", "Medium", "Low"]
        
    def load_data(self):
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f, indent=4)
    
    def display_header(self):
        """Display beautiful header with custom logo"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Your custom logo
        logo = r"""
 _   _                     _  ___  ___      _         _ _ 
| \ | |                   (_) |  \/  |     | |       | (_)
|  \| | __ _ ______ _ _ __ _  | .  . | __ _| |__   __| |_ 
| . ` |/ _` |_  / _` | '__| | | |\/| |/ _` | '_ \ / _` | |
| |\  | (_| |/ / (_| | |  | | | |  | | (_| | | | | (_| | |
\_| \_/\__,_/___\__,_|_|  |_| \_|  |_/\__,_|_| |_|\__,_|_|
"""
        console.print(Panel(logo, title="[bold magenta]Smart Task Manager[/bold magenta]", expand=False))
        console.print(Panel.fit("📝 Your Ultimate Terminal Task Manager", 
                              border_style="cyan", padding=(1, 2)))
    
    def display_stats(self):
        """Display task statistics"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task['done'])
        pending = total - completed
        
        stats_text = Text()
        stats_text.append(f"Total: {total} ", style="bold white")
        stats_text.append(f"✅ Completed: {completed} ", style="bold green")
        stats_text.append(f"⏳ Pending: {pending} ", style="bold yellow")
        
        console.print(Panel(stats_text, title="📊 Statistics", border_style="blue"))
    
    def display_tasks(self):
        """Display tasks in a beautiful table"""
        if not self.tasks:
            console.print("\n[italic yellow]No tasks yet! Time to get productive![/italic yellow]")
            return
        
        table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
        table.add_column("#", style="cyan", width=4)
        table.add_column("Task", style="green", width=35)
        table.add_column("Category", style="yellow", width=12)
        table.add_column("Priority", style="red", width=10)
        table.add_column("Date", style="blue", width=15)
        table.add_column("Status", style="magenta", width=12)
        
        for i, task in enumerate(self.tasks, 1):
            status = "✅ Done" if task['done'] else "⏳ Pending"
            priority_emoji = {
                "High": "🔴",
                "Medium": "🟡", 
                "Low": "🟢"
            }
            
            # Color code based on priority
            priority_style = {
                "High": "bold red",
                "Medium": "bold yellow",
                "Low": "bold green"
            }
            
            table.add_row(
                str(i),
                task['title'],
                f"[cyan]{task['category']}[/cyan]",
                f"[{priority_style[task['priority']]}]{priority_emoji[task['priority']]} {task['priority']}[/]",
                task['date'],
                "[bold green]✅ Done[/bold green]" if task['done'] else "[bold yellow]⏳ Pending[/bold yellow]"
            )
        
        console.print("\n")
        console.print(Panel(table, title="📋 Your Tasks", border_style="green"))
    
    def add_task(self):
        """Add a new task with beautiful prompts"""
        console.print("\n[bold underline]Add New Task[/bold underline]")
        
        title = Prompt.ask("📝 [bold green]Task description[/bold green]")
        category = Prompt.ask(
            "📂 [bold yellow]Category[/bold yellow]",
            choices=self.categories,
            default="Personal"
        )
        priority = Prompt.ask(
            "🎯 [bold red]Priority[/bold red]",
            choices=self.priorities,
            default="Medium"
        )
        
        new_task = {
            'title': title,
            'category': category,
            'priority': priority,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'done': False
        }
        
        self.tasks.append(new_task)
        self.save_data()
        console.print("[bold green]✅ Task added successfully![/bold green]")
    
    def mark_done(self):
        """Mark task as done/undone"""
        if not self.tasks:
            console.print("[yellow]No tasks to mark![/yellow]")
            return
            
        task_id = IntPrompt.ask("\n🔢 [bold]Enter task number to toggle[/bold]", default=1) - 1
        
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id]['done'] = not self.tasks[task_id]['done']
            self.save_data()
            status = "done" if self.tasks[task_id]['done'] else "pending"
            console.print(f"[bold green]✅ Task marked as {status}![/bold green]")
        else:
            console.print("[bold red]❌ Invalid task number![/bold red]")
    
    def delete_task(self):
        """Delete a task"""
        if not self.tasks:
            console.print("[yellow]No tasks to delete![/yellow]")
            return
            
        task_id = IntPrompt.ask("\n🗑️ [bold]Enter task number to delete[/bold]", default=1) - 1
        
        if 0 <= task_id < len(self.tasks):
            deleted_task = self.tasks.pop(task_id)
            self.save_data()
            console.print(f"[bold red]🗑️ Deleted: {deleted_task['title']}[/bold red]")
        else:
            console.print("[bold red]❌ Invalid task number![/bold red]")
    
    def show_menu(self):
        """Display main menu"""
        console.print("\n" + "="*50)
        console.print("[bold]MENU OPTIONS:[/bold]")
        console.print("[cyan]1.[/cyan] View Tasks")
        console.print("[cyan]2.[/cyan] Add New Task")
        console.print("[cyan]3.[/cyan] Mark Task Done/Undone")
        console.print("[cyan]4.[/cyan] Delete Task")
        console.print("[cyan]5.[/cyan] Show Statistics")
        console.print("[cyan]6.[/cyan] Exit")
        console.print("="*50)
    
    def run(self):
        """Main application loop"""
        while True:
            self.display_header()
            self.display_stats()
            self.display_tasks()
            self.show_menu()
            
            choice = Prompt.ask("\n🎯 [bold]Choose an option[/bold]", choices=["1", "2", "3", "4", "5", "6"])
            
            if choice == "1":
                continue  # Refresh display
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.mark_done()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.display_stats()
                console.input("\nPress Enter to continue...")
            elif choice == "6":
                console.print("[bold green]👋 Goodbye! Stay productive![/bold green]")
                break

# Run the application
if __name__ == "__main__":
    app = SmartTaskManager()
    app.run()