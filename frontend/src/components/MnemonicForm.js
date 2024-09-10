import React, { useState } from 'react';

function MnemonicForm({ onMnemonicGenerated }) {
  const [concept, setConcept] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL}/generate-mnemonic`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ concept }),
      });
      const data = await response.json();
      onMnemonicGenerated(data.mnemonic);
    } catch (error) {
      console.error('Error generating mnemonic:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={concept}
        onChange={(e) => setConcept(e.target.value)}
        placeholder="Enter the concept you want to remember"
        required
      />
      <button type="submit">Generate Mnemonic</button>
    </form>
  );
}

export default MnemonicForm;