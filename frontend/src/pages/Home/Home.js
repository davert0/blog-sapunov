import {useEffect} from 'react';
import styles from './Home.module.css';
import { useSelector, useDispatch } from 'react-redux';
import {thunks as articleThunks} from 'store/slices/article'


export const Article = ({ title, content }) => {
  return (
    <article className={styles.article}>
      <h2>{title}</h2>
      <p>{content}</p>
    </article>
  );
}

export const Home = () => {
  // @ts-ignore
  const articles = useSelector(state => state.article.articles);
  const dispatch = useDispatch()
  useEffect(() => {
    // @ts-ignore
    dispatch(articleThunks.getArticles());
		// eslint-disable-next-line
  }, []);
  return (
    <section className={styles.section}>
      {articles.map((article, index) => (
        <Article key={index} title={article.name} content={article.text} />
      ))}
    </section>
  );
}

