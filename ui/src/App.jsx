import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [recipes, setRecipes] = useState([]);
  const [search, setSearch] = useState(null);
  const [recommendations, setRecommendations] = useState([]);

  const getRecipies = () => {
    console.log("fetching recipes...");
    return fetch("http://localhost:8000/recepies", {
      method: "GET",
      headers: {
        "Content-Type": "application/json", // Expect JSON
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        response.json().then((res) => setRecipes(res)); // Correctly parse JSON
      })
      .catch((error) => console.error("Fetch error:", error));
  };

  const getRecommendations = (recipe) => {
    return fetch(`http://localhost:8000/more_recepies/?q=${recipe}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json", // Expect JSON
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        response.json().then((res) => {
          console.log("recommendations: ", res.documents);
          setRecommendations(res.documents[0]);
          recommendations.shift();
        }); // Correctly parse JSON
      })
      .catch((error) => console.error("Fetch error:", error));
  };

  useEffect(() => {
    getRecipies();
  }, []);

  return (
    <div className="App">
      <header className="Recipes">Recipes</header>
      <div className="RecipesContainer">
        {recipes?.map((recipe, index) => {
          var sections = recipe.split("\n");
          return (
            <div
              className="recipe"
              key={index}
              onClick={() => {
                getRecommendations(recipe);
                setSearch(index);
              }}
            >
              <span>
                <b>{sections[0]}</b>
              </span>
              <span>{sections[1]}</span>
              <span>{sections[2]}</span>
              {search === index ? (
                <div className="recommendations">
                  <div style={{marginTop:'5px', marginLeft: '4%', marginBottom: '5px'}}><b>Recommended Recipes: </b></div>
                  {recommendations.map((recommendation, index) => {
                    console.log("recommendation: ", recommendation);
                    const recommendationSections = recommendation.split("\n");
                    if (index)
                      return (
                        <div className="recommendedRecipe" key={index}>
                          <span>
                            <b>{recommendationSections[0]}</b>
                          </span>
                          <span>{recommendationSections[1]}</span>
                          <span>{recommendationSections[2]}</span>
                        </div>
                      );
                  })}
                </div>
              ) : (
                <button>Show similar recipes</button>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default App;
