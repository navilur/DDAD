import React from 'react'
import style from './recipe.module.css';

function Recipe({title,calories,image,ingredients}) {
    return (
        <div className={style.recipe}>
            <img className={style.image} src={image} alt="image"/>
            <h1>{title}</h1>
            <h2>Ingredints : </h2>
            <ol>
                {ingredients.map(ingredient =>(
                    <li>{ingredient.text}</li>
                ))}
            </ol>
            <p>{calories} cal</p>

        </div>
    )
}

export default Recipe
