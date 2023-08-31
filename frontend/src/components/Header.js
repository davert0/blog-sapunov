import React from 'react';
import styles from './Header.module.css'

const Header = () => {
  return (
    <header className={styles.header}>
      <h1>Ilya Sapunov</h1>
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/about">About</a></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;