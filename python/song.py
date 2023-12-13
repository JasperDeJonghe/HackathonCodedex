import pygame

def play_midi(midi_file):
    pygame.mixer.init()
    pygame.mixer.music.load(midi_file)
    pygame.mixer.music.play()

    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(30)


midi_file_path = "python\music\Mariah_Carey_-_All_I_Want_For_Christmas_Is_You.mid"

play_midi(midi_file_path)

