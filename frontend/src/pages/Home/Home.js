import React from 'react';
import styles from './Home.module.css';

function Article({ title, content }) {
  return (
    <article className={styles.article}>
      <h2>{title}</h2>
      <p>{content}</p>
    </article>
  );
}

function Home() {
  const articles = [
    { title: "Заголовок статьи 1", content: "Текст статьи 1..." },
    { title: "Заголовок статьи 2", content: "Текст статьи 2..." },
    { title: "Заголовок статьи 3", content: "Текст статьи 3..." }
  ];

  return (
    <section className={styles.section}>
      {articles.map((article, index) => (
        <Article key={index} title={article.title} content={article.content} />
      ))}
    </section>
  );
}

export default Home;