from dataclasses import dataclass
 
 
@dataclass(order=True)
class Movie:
    title: str
    release_year: int
    release_month: int = None
    release_day: int = None
    rating: float = None
 
    def better_than(self, other):
        return self.rating > other.rating
 
 
movie1 = Movie("Ocean's Eleven", 2001, 12, rating=7.7)
movie2 = Movie("Ocean's Eleven", 1960, rating=6.5)
 
print(movie1) # Movie(title="Ocean's Eleven", release_year=2001, release_month=12, release_day=None, rating=7.7)
print(movie2) # Movie(title="Ocean's Eleven", release_year=1960, release_month=None, release_day=None, rating=6.5)
print(movie1 < movie2) # False
print(movie1.better_than(movie2)) # True