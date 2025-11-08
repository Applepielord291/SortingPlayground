# dependencies
import gradio as gr

# Nigel Garcia
# First Created: Saturday, November 7
# Last edited: Saturday, November 8
# Project
# AI level: 0
# This is the main file. Run this to run the program.

# other scripts import
import OtherScripts.Algorithm as alg

with gr.Blocks() as demo:
    title = gr.HTML("<h1 style='text-align:center'>Sorting name goes here.</h1>") # Put a fancy image!!!!
    with gr.Row(min_height=300):
        with gr.Column():
            textBox1 = gr.Textbox(label="Array Size")
            textBox2 = gr.Textbox(label="Repeating Elements")
            textBox3 = gr.Textbox(label="Time")
            textbox4 = gr.Textbox(label="rand vals")
        with gr.Column():
            display = gr.Image()
    with gr.Row():
        with gr.Column(min_width=50): #gap
            pass
        with gr.Column(scale=0):
            startSimulationBtn = gr.Button("Start")
        with gr.Column(min_width=200): # Gap
            pass

demo.launch()
