
import chromadb
# from openai.embeddings_utils import get_embedding

recepies = [
    "Spaghetti Carbonara\nIngredients: Spaghetti, eggs, Parmesan cheese, pancetta, black pepper.\nInstructions: Cook spaghetti, fry pancetta, mix eggs and cheese, combine, and serve hot.",
    "Chicken Curry\nIngredients: Chicken, onions, tomatoes, garlic, ginger, curry powder, coconut milk.\nInstructions: Sauté onions, garlic, and ginger. Add chicken and curry powder, then tomatoes and coconut milk. Simmer until tender.",
    "Caprese Salad\nIngredients: Tomatoes, mozzarella, basil, olive oil, balsamic vinegar.\nInstructions: Slice tomatoes and mozzarella. Layer with basil, drizzle with olive oil and balsamic vinegar.",
    "Beef Tacos\nIngredients: Ground beef, taco seasoning, tortillas, lettuce, cheese, salsa.\nInstructions: Cook beef with seasoning. Assemble tacos with desired toppings.",
    "Veggie Stir-Fry\nIngredients: Mixed vegetables, soy sauce, garlic, ginger, sesame oil.\nInstructions: Stir-fry vegetables with garlic and ginger. Add soy sauce and sesame oil. Serve with rice.",
    "Margherita Pizza\nIngredients: Pizza dough, tomato sauce, mozzarella, basil, olive oil.\nInstructions: Spread sauce on dough, add cheese and basil, bake at 475°F (245°C) until crust is golden.",
    "Chicken Alfredo Pasta\nIngredients: Chicken, fettuccine, cream, butter, Parmesan, garlic.\nInstructions: Cook pasta, sauté chicken and garlic, make sauce with cream and cheese. Mix everything together.",
    "Greek Salad\nIngredients: Cucumbers, tomatoes, feta, olives, red onion, olive oil, oregano.\nInstructions: Chop vegetables, add feta and olives, drizzle with olive oil and sprinkle oregano.",
    "Pancakes\nIngredients: Flour, milk, eggs, sugar, baking powder, butter.\nInstructions: Mix ingredients, pour batter onto griddle, cook until golden brown on both sides.",
    "Chocolate Chip Cookies\nIngredients: Flour, sugar, brown sugar, butter, eggs, chocolate chips, baking soda, vanilla extract.\nInstructions: Cream butter and sugars, add eggs and vanilla. Mix dry ingredients, fold in chocolate chips. Bake at 350°F (175°C) for 10-12 minutes."
]
metadata = [
    {"source": "SomeSource1"},
    {"source": "SomeSource2"},
    {"source": "SomeSource3"},
    {"source": "SomeSource3"},
    {"source": "SomeSource2"},
    {"source": "SomeSource1"},
    {"source": "SomeSource1"},
    {"source": "SomeSource1"},
    {"source": "SomeSource2"},
    {"source": "SomeSource3"},
]

def seed_db(collection):
    collection.add(documents=recepies, metadatas=metadata, ids=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

def query_db(query_text, collection):
    results = collection.query(
        query_texts=query_text, # Chroma will embed this for you
        n_results=2 # how many results to return
    )

    print(results)
    

client = chromadb.Client()
# collection = client.create_collection(name="recepies")
client.delete_collection(name="recepies")
# seed_db(collection)
# query_db(["Spaghetti Carbonara"], collection)
