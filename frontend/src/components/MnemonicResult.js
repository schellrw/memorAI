import React from 'react';

function MnemonicResult({ mnemonic }) {
  return (
    <div>
      <h2>Generated Mnemonic:</h2>
      <p>{mnemonic}</p>
    </div>
  );
}

export default MnemonicResult;