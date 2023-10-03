import styles from './About.module.css';
import React from 'react';

const text = "Привет! Меня зовут Илья Сапунов, и я идентифицирую себя как разработчик программного обеспечения :) Здесь я буду писать в основном о тех вещах, которые меня интересуют, и в которых мне бы хотелось разобраться."

const About = () => {
    return (
      <div className={styles.container}>
        <h1 className={styles.title}>Обо мне</h1>
        <p className={styles.description}>{text}</p>
      </div>
    );
  };
  
  export default About;