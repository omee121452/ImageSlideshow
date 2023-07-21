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
            TempNode = Node(os.path.join('images', imagePath))
            if not self.head:  # this is the same as saying if self.head == None
                self.head = TempNode
                self.current_node = TempNode
            else:
                self.current_node.next = TempNode
                self.current_node = TempNode
        self.current_node = self.head  # reseting the current node to be the head so when we use the nodes later it is in order and starts from the head.

    def display_image(self):
        if self.current_node:
            Image = pygame.image.load(self.current_node.image_path)
            scaledImage = pygame.transform.scale(Image, (self.width, self.height))
            self.screen.blit(scaledImage, (0, 0))
            pygame.display.flip()

    def next_image(self):
        print('NextImg')
        if self.current_node.next:
            self.current_node = self.current_node.next
        else:
            self.current_node = self.head
        self.display_image()

    def prev_image(self):
        print('PreviousImg')
        temporaryNode = self.head
        if self.current_node == self.head:
            while temporaryNode.next is not None:
                temporaryNode = temporaryNode.next
        else:
            while temporaryNode.next != self.current_node:
                temporaryNode = temporaryNode.next

        self.current_node = temporaryNode
        self.display_image()

    def run(self):
        running = True
        while running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.prev_image()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.next_image()
            self.clock.tick(30)


# Create the Slideshow object 1
slideshow = Slideshow()
# commitandpush
# Run the slideshow
slideshow.run()
