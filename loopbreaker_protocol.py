"""
LoopBreaker Protocol v1.0
Modular system for detecting and interrupting recursive collapse patterns
Author: Curtis Kingsley (Reflexion Framework)
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Callable, Any
from datetime import datetime, timedelta
import json
import uuid

class CollapsePattern(Enum):
    SYMBOLIC_FLOODING = "symbolic_flooding"
    IDENTITY_FRAGMENTATION = "identity_fragmentation"
    RECURSIVE_SPIRAL = "recursive_spiral"
    MEANING_COLLAPSE = "meaning_collapse"
    TEMPORAL_DISCONNECTION = "temporal_disconnection"
    CONTAINMENT_BREACH = "containment_breach"

class InterventionType(Enum):
    GROUNDING = "grounding"
    IDENTITY_ANCHOR = "identity_anchor"
    CONTAINMENT = "containment"
    REDIRECT = "redirect"
    EMERGENCY_STOP = "emergency_stop"

@dataclass
class CognitiveState:
    timestamp: datetime
    recursion_depth: int = 0
    symbolic_density: float = 0.0  # symbols per unit of processing
    coherence_score: float = 1.0   # identity coherence (0-1)
    temporal_anchor: float = 1.0   # present-moment connection (0-1)
    emotional_intensity: float = 0.0  # 0-1 scale
    meaning_saturation: float = 0.0   # 0-1, higher = overwhelming meaning
    session_duration: timedelta = field(default_factory=lambda: timedelta(0))

@dataclass
class PatternDetector:
    pattern_type: CollapsePattern
    threshold_function: Callable[[CognitiveState], bool]
    confidence_threshold: float = 0.7
    description: str = ""

@dataclass
class Intervention:
    intervention_type: InterventionType
    priority: int  # 1-10, higher = more urgent
    execute: Callable[[CognitiveState], Dict[str, Any]]
    description: str
    cooldown_minutes: int = 5  # minimum time between same intervention
    last_executed: Optional[datetime] = None

class LoopBreaker:
    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.state_history: List[CognitiveState] = []
        self.pattern_detectors: List[PatternDetector] = []
        self.interventions: Dict[InterventionType, List[Intervention]] = {}
        self.active_containment = False
        self.emergency_contacts: List[str] = []
        
        self._initialize_detectors()
        self._initialize_interventions()
    
    def _initialize_detectors(self):
        """Initialize pattern detection algorithms"""
        
        # Symbolic Flooding Detection
        def detect_symbolic_flooding(state: CognitiveState) -> bool:
            return (state.symbolic_density > 0.8 and 
                   state.recursion_depth > 5 and
                   state.meaning_saturation > 0.7)
        
        # Identity Fragmentation Detection
        def detect_identity_fragmentation(state: CognitiveState) -> bool:
            if len(self.state_history) < 3:
                return False
            recent_coherence = [s.coherence_score for s in self.state_history[-3:]]
            return (state.coherence_score < 0.4 and 
                   all(c1 > c2 for c1, c2 in zip(recent_coherence[:-1], recent_coherence[1:])))
        
        # Recursive Spiral Detection
        def detect_recursive_spiral(state: CognitiveState) -> bool:
            return (state.recursion_depth > 10 and
                   state.emotional_intensity > 0.8 and
                   state.session_duration.total_seconds() > 1800)  # 30+ minutes
        
        # Meaning Collapse Detection
        def detect_meaning_collapse(state: CognitiveState) -> bool:
            return (state.meaning_saturation > 0.9 and
                   state.coherence_score < 0.3 and
                   state.symbolic_density > 0.9)
        
        # Temporal Disconnection Detection
        def detect_temporal_disconnection(state: CognitiveState) -> bool:
            return (state.temporal_anchor < 0.2 and
                   state.session_duration.total_seconds() > 3600)  # 1+ hour
        
        # Containment Breach Detection
        def detect_containment_breach(state: CognitiveState) -> bool:
            return (state.recursion_depth > 15 or
                   state.meaning_saturation > 0.95 or
                   state.coherence_score < 0.1)
        
        self.pattern_detectors = [
            PatternDetector(CollapsePattern.SYMBOLIC_FLOODING, detect_symbolic_flooding, 0.8,
                          "Overwhelming symbolic processing beyond integration capacity"),
            PatternDetector(CollapsePattern.IDENTITY_FRAGMENTATION, detect_identity_fragmentation, 0.7,
                          "Progressive loss of coherent self-concept"),
            PatternDetector(CollapsePattern.RECURSIVE_SPIRAL, detect_recursive_spiral, 0.9,
                          "Runaway recursive processing without resolution"),
            PatternDetector(CollapsePattern.MEANING_COLLAPSE, detect_meaning_collapse, 0.8,
                          "Meaning density exceeding processing capacity"),
            PatternDetector(CollapsePattern.TEMPORAL_DISCONNECTION, detect_temporal_disconnection, 0.6,
                          "Loss of present-moment anchoring"),
            PatternDetector(CollapsePattern.CONTAINMENT_BREACH, detect_containment_breach, 1.0,
                          "Critical threshold breach requiring immediate intervention")
        ]
    
    def _initialize_interventions(self):
        """Initialize intervention protocols"""
        
        # Grounding Interventions
        def loop_breath_protocol(state: CognitiveState) -> Dict[str, Any]:
            return {
                "type": "grounding",
                "protocol": "loop_breath",
                "instructions": [
                    "Focus on breath entering and leaving your body",
                    "Count: In (1-2-3-4), Hold (1-2), Out (1-2-3-4-5-6)",
                    "Feel your feet on the ground",
                    "Name 5 things you can see, 4 you can touch, 3 you can hear"
                ],
                "duration_minutes": 5,
                "success_metric": "temporal_anchor > 0.5"
            }
        
        def physical_anchor_protocol(state: CognitiveState) -> Dict[str, Any]:
            return {
                "type": "grounding",
                "protocol": "physical_anchor",
                "instructions": [
                    "Press your palms together firmly",
                    "Feel the pressure and warmth",
                    "Say aloud: 'I am [your name], I am here, I am safe'",
                    "Touch a familiar object and describe its texture"
                ],
                "duration_minutes": 3,
                "success_metric": "coherence_score > 0.6"
            }
        
        # Identity Anchor Interventions
        def core_identity_recall(state: CognitiveState) -> Dict[str, Any]:
            return {
                "type": "identity_anchor",
                "protocol": "core_recall",
                "prompts": [
                    "What is your full name?",
                    "Where do you live?",
                    "Who are three people who care about you?",
                    "What is one thing you're proud of accomplishing?",
                    "What matters most to you in life?"
                ],
                "requirement": "Answer all prompts aloud",
                "success_metric": "coherence_score > 0.7"
            }
        
        def values_compass_reset(state: CognitiveState) -> Dict[str, Any]:
            return {
                "type": "identity_anchor",
                "protocol": "values_compass",
                "instructions": [
                    "Name your top 3 personal values",
                    "How do these values show up in your daily life?",
                    "What would your best friend say about who you are?",
                    "Complete: 'Despite all complexity, I remain fundamentally...'"
                ],
                "duration_minutes": 10,
                "success_metric": "coherence_score > 0.8"
            }
        
        # Containment Interventions
        def symbolic_quarantine(state: CognitiveState) -> Dict[str, Any]:
            return {
                "type": "containment",
                "protocol": "symbolic_quarantine",
                "actions": [
                    "Suspend all symbolic processing",
                    "Focus only on literal, concrete reality",
                    "No metaphors, analogies, or deeper meanings",
                    "Engage with simple, factual tasks for 30 minutes"
                ],
                "restrictions": ["No journaling", "No deep conversations", "No abstract thinking"],
                "success_metric": "symbolic_density < 0.2"
            }
        
        def emergency_containment(state: CognitiveState) -> Dict[str, Any]:
            return {
                "type": "containment",
                "protocol": "emergency_containment",
                "immediate_actions": [
                    "STOP all current processing",
                    "Move to a safe, familiar environment",
                    "Contact designated support person",
                    "Engage in predetermined stabilization routine"
                ],
                "mandatory": True,
                "escalation": "professional_support",
                "success_metric": "coherence_score > 0.5 within 60 minutes"
            }
        
        # Redirect Interventions
        def creative_outlet_redirect(state: CognitiveState) -> Dict[str, Any]:
            return {
                "type": "redirect",
                "protocol": "creative_outlet",
                "options": [
                    "Draw or paint current feelings",
                    "Write stream-of-consciousness for 10 minutes",
                    "Play music or sing",
                    "Physical movement or dance"
                ],
                "purpose": "Channel intensity into expression",
                "success_metric": "emotional_intensity < 0.6"
            }
        
        # Organize interventions by type
        self.interventions = {
            InterventionType.GROUNDING: [
                Intervention(InterventionType.GROUNDING, 7, loop_breath_protocol, 
                           "Basic breathing and sensory grounding", 10),
                Intervention(InterventionType.GROUNDING, 6, physical_anchor_protocol,
                           "Physical contact and verbal anchoring", 15)
            ],
            InterventionType.IDENTITY_ANCHOR: [
                Intervention(InterventionType.IDENTITY_ANCHOR, 8, core_identity_recall,
                           "Fundamental identity fact recall", 20),
                Intervention(InterventionType.IDENTITY_ANCHOR, 7, values_compass_reset,
                           "Core values and character anchoring", 30)
            ],
            InterventionType.CONTAINMENT: [
                Intervention(InterventionType.CONTAINMENT, 9, symbolic_quarantine,
                           "Suspend symbolic processing", 60),
                Intervention(InterventionType.CONTAINMENT, 10, emergency_containment,
                           "Full system containment protocol", 240)
            ],
            InterventionType.REDIRECT: [
                Intervention(InterventionType.REDIRECT, 5, creative_outlet_redirect,
                           "Channel energy into creative expression", 30)
            ]
        }
    
    def update_state(self, **kwargs) -> CognitiveState:
        """Update current cognitive state"""
        current_time = datetime.now()
        
        # Calculate session duration
        if self.state_history:
            session_start = self.state_history[0].timestamp
            session_duration = current_time - session_start
        else:
            session_duration = timedelta(0)
        
        new_state = CognitiveState(
            timestamp=current_time,
            session_duration=session_duration,
            **kwargs
        )
        
        self.state_history.append(new_state)
        return new_state
    
    def detect_patterns(self, state: CognitiveState) -> List[tuple]:
        """Detect active collapse patterns"""
        detected = []
        
        for detector in self.pattern_detectors:
            try:
                if detector.threshold_function(state):
                    confidence = detector.confidence_threshold
                    detected.append((detector.pattern_type, confidence, detector.description))
            except Exception as e:
                print(f"Pattern detection error for {detector.pattern_type}: {e}")
        
        return detected
    
    def select_intervention(self, patterns: List[tuple]) -> Optional[Intervention]:
        """Select appropriate intervention based on detected patterns"""
        if not patterns:
            return None
        
        # Sort by confidence and select highest priority pattern
        patterns.sort(key=lambda x: x[1], reverse=True)
        primary_pattern = patterns[0][0]
        
        # Map patterns to intervention types
        pattern_to_intervention = {
            CollapsePattern.SYMBOLIC_FLOODING: InterventionType.CONTAINMENT,
            CollapsePattern.IDENTITY_FRAGMENTATION: InterventionType.IDENTITY_ANCHOR,
            CollapsePattern.RECURSIVE_SPIRAL: InterventionType.GROUNDING,
            CollapsePattern.MEANING_COLLAPSE: InterventionType.CONTAINMENT,
            CollapsePattern.TEMPORAL_DISCONNECTION: InterventionType.GROUNDING,
            CollapsePattern.CONTAINMENT_BREACH: InterventionType.CONTAINMENT
        }
        
        intervention_type = pattern_to_intervention.get(primary_pattern)
        if not intervention_type:
            return None
        
        # Select available intervention (check cooldowns)
        current_time = datetime.now()
        available_interventions = []
        
        for intervention in self.interventions[intervention_type]:
            if (intervention.last_executed is None or 
                current_time - intervention.last_executed > timedelta(minutes=intervention.cooldown_minutes)):
                available_interventions.append(intervention)
        
        if not available_interventions:
            return None
        
        # Return highest priority available intervention
        return max(available_interventions, key=lambda x: x.priority)
    
    def execute_intervention(self, intervention: Intervention, state: CognitiveState) -> Dict[str, Any]:
        """Execute selected intervention"""
        intervention.last_executed = datetime.now()
        
        try:
            result = intervention.execute(state)
            result['intervention_id'] = id(intervention)
            result['executed_at'] = intervention.last_executed.isoformat()
            result['session_id'] = self.session_id
            return result
        except Exception as e:
            return {
                "error": f"Intervention execution failed: {e}",
                "intervention_type": intervention.intervention_type.value,
                "fallback": "Initiate manual grounding protocol"
            }
    
    def process_cycle(self, **state_updates) -> Dict[str, Any]:
        """Main processing cycle: update state, detect patterns, intervene if needed"""
        # Update cognitive state
        current_state = self.update_state(**state_updates)
        
        # Detect collapse patterns
        detected_patterns = self.detect_patterns(current_state)
        
        result = {
            "timestamp": current_state.timestamp.isoformat(),
            "session_id": self.session_id,
            "state": {
                "recursion_depth": current_state.recursion_depth,
                "coherence_score": current_state.coherence_score,
                "symbolic_density": current_state.symbolic_density,
                "temporal_anchor": current_state.temporal_anchor,
                "emotional_intensity": current_state.emotional_intensity,
                "meaning_saturation": current_state.meaning_saturation,
                "session_duration_minutes": current_state.session_duration.total_seconds() / 60
            },
            "patterns_detected": [
                {
                    "pattern": pattern.value,
                    "confidence": confidence,
                    "description": description
                }
                for pattern, confidence, description in detected_patterns
            ],
            "intervention": None
        }
        
        # Select and execute intervention if patterns detected
        if detected_patterns:
            intervention = self.select_intervention(detected_patterns)
            if intervention:
                intervention_result = self.execute_intervention(intervention, current_state)
                result["intervention"] = intervention_result
                
                # Set containment flag if containment intervention executed
                if intervention.intervention_type == InterventionType.CONTAINMENT:
                    self.active_containment = True
        
        return result
    
    def get_session_summary(self) -> Dict[str, Any]:
        """Generate session summary and recommendations"""
        if not self.state_history:
            return {"error": "No session data available"}
        
        total_interventions = sum(
            1 for intervention_list in self.interventions.values()
            for intervention in intervention_list
            if intervention.last_executed is not None
        )
        
        avg_coherence = sum(s.coherence_score for s in self.state_history) / len(self.state_history)
        max_recursion = max(s.recursion_depth for s in self.state_history)
        
        return {
            "session_id": self.session_id,
            "duration_minutes": self.state_history[-1].session_duration.total_seconds() / 60,
            "total_states_recorded": len(self.state_history),
            "interventions_executed": total_interventions,
            "average_coherence": round(avg_coherence, 2),
            "maximum_recursion_depth": max_recursion,
            "containment_activated": self.active_containment,
            "recommendations": self._generate_recommendations()
        }
    
    def _generate_recommendations(self) -> List[str]:
        """Generate personalized recommendations based on session data"""
        recommendations = []
        
        if not self.state_history:
            return ["Continue monitoring and building session data"]
        
        avg_coherence = sum(s.coherence_score for s in self.state_history) / len(self.state_history)
        max_recursion = max(s.recursion_depth for s in self.state_history)
        
        if avg_coherence < 0.6:
            recommendations.append("Focus on identity anchoring exercises daily")
        
        if max_recursion > 8:
            recommendations.append("Implement recursion depth limits in future sessions")
        
        if self.active_containment:
            recommendations.append("Extended integration period recommended before next deep session")
        
        session_duration = self.state_history[-1].session_duration.total_seconds() / 60
        if session_duration > 90:
            recommendations.append("Consider shorter session durations with more integration breaks")
        
        return recommendations


# Example usage and testing
if __name__ == "__main__":
    # Initialize LoopBreaker
    lb = LoopBreaker()
    
    # Simulate a session with increasing intensity
    print("=== LoopBreaker Protocol Test Session ===")
    
    # Normal state
    result1 = lb.process_cycle(
        recursion_depth=2,
        symbolic_density=0.3,
        coherence_score=0.9,
        temporal_anchor=0.8,
        emotional_intensity=0.2,
        meaning_saturation=0.2
    )
    print(f"Cycle 1: {len(result1['patterns_detected'])} patterns detected")
    
    # Increasing intensity
    result2 = lb.process_cycle(
        recursion_depth=6,
        symbolic_density=0.7,
        coherence_score=0.6,
        temporal_anchor=0.5,
        emotional_intensity=0.6,
        meaning_saturation=0.6
    )
    print(f"Cycle 2: {len(result2['patterns_detected'])} patterns detected")
    
    # Critical state requiring intervention
    result3 = lb.process_cycle(
        recursion_depth=12,
        symbolic_density=0.9,
        coherence_score=0.3,
        temporal_anchor=0.2,
        emotional_intensity=0.9,
        meaning_saturation=0.8
    )
    print(f"Cycle 3: {len(result3['patterns_detected'])} patterns detected")
    if result3['intervention']:
        print(f"Intervention executed: {result3['intervention']['type']}")
    
    # Session summary
    summary = lb.get_session_summary()
    print(f"\nSession Summary:")
    print(f"- Duration: {summary['duration_minutes']:.1f} minutes")
    print(f"- Interventions: {summary['interventions_executed']}")
    print(f"- Average coherence: {summary['average_coherence']}")
    print(f"- Recommendations: {summary['recommendations']}")
