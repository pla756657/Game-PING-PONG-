#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
  def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
      super().__init__()
      self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
      self.speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y

  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
  def update_r(self):
      keys = key.get_pressed()
      if keys[K_UP] and self.rect.y > 5:
        self.rect.y -= self.speed
      if keys[K_DOWN] and self.rect.y < win_height - 80:
        self.rect.y += self.speed
  def update_l(self):
      keys = key.get_pressed()
      if keys[K_w] and self.rect.y > 5:
        self.rect.y -= self.speed
      if keys[K_s] and self.rect.y < win_height - 80:
        self.rect.y += self.speed
  #игровая сцена
  back = (200, 255, 255)
  win_width = 600
  win_height = 600
  window = display.set_mode((win_width, win_height))
  window.fill(back)
  
  
  #флаги, отвечающие за состояние игры
  game = True
  finish = False
  clock = time.Clock()
  FPS = 60
  
  
  #создание ракетки и мяча
  racket_1 = Player('racket.png', 30, 200, 4, 50, 150)
  racket_2 = Player('racket.png', 520, 200, 4, 50, 150)
  ball = GameSprite('tennis_ball.png', 200, 200, 4, 50, 50)
  
  font.init()
  font = font.Font(None, 35)
  lose_1 = font.render('PLAYER_1 LOSE!!!', True, (180, 0, 0))
  lose_2 = font.render('PLAYER_2 LOSE!!!', True, (180, 0, 0))
  speed_x = 3
  speed_y = 3
  
