import React from 'react';

const Footer = () => {
  return (
    <footer className="absolute bottom-0 left-0 w-full bg-gray-50 py-1 z-1 text-sm shadow-sm">
      <div className="container mx-auto text-center">
        <span>&copy; {new Date().getFullYear()} Todos os direitos reservados.</span>
      </div>
    </footer>
  );
};

export default Footer;
