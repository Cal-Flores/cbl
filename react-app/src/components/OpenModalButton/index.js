import React from 'react';
import { useModal } from '../../context/Modal';

function OpenModalButton({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed
  fighter, // Receive data as a prop
  
}) {
  const { setModalContent, setOnModalClose } = useModal();



  return (
    <button onClick={() => setModalContent(React.createElement(modalComponent, { fighter }))}>{buttonText}</button>
  );
}

export default OpenModalButton;
