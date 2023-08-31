import React from 'react';
import styles from './Home.module.css';
import { useSelector } from 'react-redux';


export const Article = ({ title, content }) => {
  return (
    <article className={styles.article}>
      <h2>{title}</h2>
      <p>{content}</p>
    </article>
  );
}

export const Home = () => {
  const articles = useSelector(state => state.article.articles);

  return (
    <section className={styles.section}>
      {articles.map((article, index) => (
        <Article key={index} title={article.title} content={article.content} />
      ))}
    </section>
  );
}

