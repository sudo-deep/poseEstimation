import React from 'react'

const App = () => {

  const handleRunApp = async() => {
    try {
      const response = await fetch('http://127.0.0.1:5000/pose-estimation', {
        method: 'POST'
      })
      if(response.ok){
        console.log('Running')
      }else{
        console.log('error');
      }
    } catch (error) {
      console.log(error.message)
    }
  }
  return (
    <div>
      <button onClick={handleRunApp}>
        Run Pose Estimation
      </button>
    </div>
  )
}

export default App