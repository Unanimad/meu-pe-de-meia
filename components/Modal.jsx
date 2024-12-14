import React from 'react';
import { Modal as MantineModal, Button } from '@mantine/core';

const Modal = ({ isOpen, onClose, title, children }) => {
  return (
    <MantineModal opened={isOpen} onClose={onClose} centered>
      <strong>{title}</strong>
      {children}
      <Button onClick={onClose} className="mt-4">
        Fechar
      </Button>
    </MantineModal>
  );
};

export default Modal;