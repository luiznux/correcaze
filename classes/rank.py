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
        with open(self.__RANKING_FILE, "w") as fp:
            json.dump({}, fp)

    def write_to_scoreboard(self, player_name: str, points: int) -> None:
        with open(self.__RANKING_FILE) as ranking_file:
            rankings = json.load(ranking_file)
        rankings.update({"name": player_name, "points": points})

        with open(self.__RANKING_FILE, "w") as ranking_file:
            json.dump(ranking_file, rankings)

    def read_scoreboard(self) -> List[PlayerRank]:
        ranks: List[PlayerRank] = []
        with open(self.__RANKING_FILE) as ranking_file:
            rankings = json.load(ranking_file)
            for ranking in rankings:
                ranks.append(PlayerRank(ranking["name"], int(ranking["points"])))

        return ranks
