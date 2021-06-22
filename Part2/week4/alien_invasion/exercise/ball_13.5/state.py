class State():
    def __init__(self, settings):
        self.settings = settings

        # 每次重新运行都进行重置
        self.reset_game()
        # 表示游戏是否可以继续执行
        self.game_state = True

    def reset_game(self):
        self.opportunity = self.settings.state
