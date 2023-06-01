import pygame
import os

class Node:
    def __init__(self, image_path, next=None):
        self.image_path = image_path
        self.next = next


class Slideshow:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.current_node = None
        self.head = None
        self.add_images()
        self.display_image()

    def add_images(self):
        for imagePath in os.listdir('images'):
            print(imagePath)
            TempNode = Node(imagePath)
            if not self.head: #this is the same as saying if self.head == None
                self.head=TempNode
                self.current_node = TempNode
            else:
                self.current_node.next = TempNode
                self.current_node = TempNode
        self.current_node = self.head




    def display_image(self):
        pass

    def next_image(self):
        pass

    def prev_image(self):
        pass

    def run(self):
        running = True
        while running == True:
            pass


# Create the Slideshow object
slideshow = Slideshow()
#commitandpush
# Run the slideshow
slideshow.run()