import pyxel

GAME_TITLE = "HauntedDash"

CHICK_SPEED_x = 0.06
CHICK_SPEED_y = 0.04
CHICK_SPAWN_INTERVAL = 150

class HauntedDash:
    def __init__(self):
        pyxel.init(160, 120, title=GAME_TITLE)

        # ゲームをリセット
        self.is_title = True
        self.reset_game()

        # アプリの実行
        pyxel.run(self.update, self.draw)

    # ゲームのリセット
    def reset_game(self):
        self.score = 0

        self.timer = 0

        self.chick_x = (pyxel.width - 8) / 2
        self.chick_y = pyxel.height / 4
        self.chick_vx = 0
        self.chick_vy = 0
        self.chick_dir = 1 # ヒヨコの左右の向き

        # マップの配置を初期化
        self.ghost = []
    
    def update(self):
        pass

    def draw(self):
        pass

HauntedDash()
