import json
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class PlayerRank:
    name: str
    points: int


class Ranking:
    __RANKING_FILE = "data/ranking.json"

    def __init__(self):
        Path("data").mkdir(exist_ok=True)
        ranking_file = Path(self.__RANKING_FILE)
        if not ranking_file.exists():
            with open(self.__RANKING_FILE, "w") as fp:
                json.dump({"rankings": []}, fp)

    def write_to_scoreboard(self, player_name: str, points: int) -> None:
        with open(self.__RANKING_FILE) as ranking_file:
            rankings = json.load(ranking_file)
        rankings["rankings"].append({"name": player_name, "points": points})

        with open(self.__RANKING_FILE, "w") as ranking_file:
            json.dump(rankings, ranking_file)

    def read_scoreboard(self) -> List[PlayerRank]:
        ranks: List[PlayerRank] = []
        with open(self.__RANKING_FILE) as ranking_file:
            rankings = json.load(ranking_file)
            for ranking in rankings["rankings"]:
                ranks.append(PlayerRank(ranking["name"], int(ranking["points"])))

        return ranks
