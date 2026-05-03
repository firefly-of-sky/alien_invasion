from pathlib import Path
import json

class GameStats:
    """跟踪游戏的统计信息"""
    
    def __init__(self, ai_game):
        """初始化统计信息"""

        # 在任何条件下都不应该重置最高分
        self.read_high_score()

        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        """读取json文件中的最高分"""
        path = Path('high_score.json')
        contents = path.read_text()
        try:
            self.high_score = json.loads(contents)
        except json.decoder.JSONDecodeError:
            self.high_score = 0