import React from 'react';
import styles from './Footer.module.css';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGithub } from "@fortawesome/free-brands-svg-icons";

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <p>
        © {new Date().getFullYear()} <a href="mailto:ilya.v.sapunov@gmail.com">Ilya Sapunov </a>
        <a href="https://github.com/davert0">
          <FontAwesomeIcon icon={faGithub} />
        </a>
      </p>
    </footer>
  );
};

export default Footer;