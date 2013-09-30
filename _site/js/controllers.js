//Controller
//Load data from parse and store it in models
/* Parse REST API
  curl -X GET \
  -H "X-Parse-Application-Id: 19jwtpLsqoJhbLsf24WDTE2Js8kc0bMBGFxdlOeC" \
  -H "X-Parse-REST-API-Key: 1ZoYipWcTLMPm2OzsQYDOsOAQu9qYOmPI2IhCB37" \
  https://api.parse.com/1/classes/GameScore/Ed1nuqPvcm
*/

angular.module('exercisesModule',[ngResource]).
  factory('Exercise', function($resource){
    return $resource('',{},{
      query:{method:'GET',params:{exerciseId:''},isArray:true}
    });
  });

function processExerciseData(rawExercisesArray){
  numberOfRows = Math.ceil(rawExercisesArray.length/4)
  finalExerciseArray=[]
  for(i=0;i<numberOfRows;i++){
    finalExerciseArray.push(rawExercisesArray.slice(i*4,4*(i+1)));
  }
  return finalExerciseArray;
}

function ExercisesListController($scope){
  exercises = [{'numOfStars':0},
                {'numOfStars':1},
                {'numOfStars':2},
                {'numOfStars':3},
                {'numOfStars':4},
                {'numOfStars':5},
                {'numOfStars':6},
                {'numOfStars':7},
                {'numOfStars':8},
                {'numOfStars':9}]
  $scope.exerciseData = processExerciseData(exercises)
}
