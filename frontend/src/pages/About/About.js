import styles from './About.module.css';
import React from 'react';

const About = () => {
    return (
      <div className={styles.container}>
        <h1 className={styles.title}>About</h1>
        <p className={styles.description}>This is the About page.</p>
      </div>
    );
  };
  
  export default About;