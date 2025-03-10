# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AbstractiveSummarizationLROResult
from ._models_py3 import AbstractiveSummarizationLROTask
from ._models_py3 import AbstractiveSummarizationResult
from ._models_py3 import AbstractiveSummarizationResultBase
from ._models_py3 import AbstractiveSummarizationTaskParameters
from ._models_py3 import AbstractiveSummarizationTaskParametersBase
from ._models_py3 import AbstractiveSummary
from ._models_py3 import AbstractiveSummaryDocumentResult
from ._models_py3 import AbstractiveSummaryDocumentResultWithDetectedLanguage
from ._patch import AgeResolution
from ._models_py3 import AnalyzeTextDynamicClassificationInput
from ._models_py3 import AnalyzeTextEntityLinkingInput
from ._models_py3 import AnalyzeTextEntityRecognitionInput
from ._models_py3 import AnalyzeTextJobState
from ._models_py3 import AnalyzeTextJobStatistics
from ._models_py3 import AnalyzeTextJobsInput
from ._models_py3 import AnalyzeTextKeyPhraseExtractionInput
from ._models_py3 import AnalyzeTextLROResult
from ._models_py3 import AnalyzeTextLROTask
from ._models_py3 import AnalyzeTextLanguageDetectionInput
from ._models_py3 import AnalyzeTextPiiEntitiesRecognitionInput
from ._models_py3 import AnalyzeTextSentimentAnalysisInput
from ._models_py3 import AnalyzeTextTask
from ._models_py3 import AnalyzeTextTaskResult
from ._patch import AreaResolution
from ._models_py3 import BaseResolution
from ._models_py3 import ClassificationDocumentResult
from ._models_py3 import ClassificationResult
from ._patch import CurrencyResolution
from ._models_py3 import CustomEntitiesLROTask
from ._models_py3 import CustomEntitiesResult
from ._models_py3 import CustomEntitiesResultDocumentsItem
from ._models_py3 import CustomEntitiesTaskParameters
from ._models_py3 import CustomEntityRecognitionLROResult
from ._models_py3 import CustomLabelClassificationResult
from ._models_py3 import CustomLabelClassificationResultDocumentsItem
from ._models_py3 import CustomMultiLabelClassificationLROResult
from ._models_py3 import CustomMultiLabelClassificationLROTask
from ._models_py3 import CustomMultiLabelClassificationTaskParameters
from ._models_py3 import CustomResult
from ._models_py3 import CustomSingleLabelClassificationLROResult
from ._models_py3 import CustomSingleLabelClassificationLROTask
from ._models_py3 import CustomSingleLabelClassificationTaskParameters
from ._models_py3 import CustomTaskParameters
from ._patch import DateTimeResolution
from ._models_py3 import DetectedLanguage
from ._models_py3 import DocumentDetectedLanguage
from ._models_py3 import DocumentDetectedLanguageString
from ._models_py3 import DocumentError
from ._models_py3 import DocumentRequestStatistics
from ._models_py3 import DocumentResult
from ._models_py3 import DocumentStatistics
from ._models_py3 import DocumentWarning
from ._models_py3 import DynamicClassificationDocumentResult
from ._models_py3 import DynamicClassificationResult
from ._models_py3 import DynamicClassificationResultDocumentsItem
from ._models_py3 import DynamicClassificationTaskParameters
from ._models_py3 import DynamicClassificationTaskResult
from ._models_py3 import EntitiesDocumentResult
from ._models_py3 import EntitiesLROTask
from ._models_py3 import EntitiesResult
from ._models_py3 import EntitiesResultWithDetectedLanguage
from ._models_py3 import EntitiesTaskParameters
from ._models_py3 import EntitiesTaskResult
from ._models_py3 import Entity
from ._models_py3 import EntityLinkingLROResult
from ._models_py3 import EntityLinkingLROTask
from ._models_py3 import EntityLinkingResult
from ._models_py3 import EntityLinkingResultWithDetectedLanguage
from ._models_py3 import EntityLinkingTaskParameters
from ._models_py3 import EntityLinkingTaskResult
from ._models_py3 import EntityRecognitionLROResult
from ._models_py3 import EntityWithResolution
from ._models_py3 import Error
from ._models_py3 import ErrorResponse
from ._models_py3 import ExtractedSummaryDocumentResult
from ._models_py3 import ExtractedSummaryDocumentResultWithDetectedLanguage
from ._models_py3 import ExtractedSummarySentence
from ._models_py3 import ExtractiveSummarizationLROResult
from ._models_py3 import ExtractiveSummarizationLROTask
from ._models_py3 import ExtractiveSummarizationResult
from ._models_py3 import ExtractiveSummarizationTaskParameters
from ._models_py3 import HealthcareAssertion
from ._models_py3 import HealthcareEntitiesDocumentResult
from ._models_py3 import HealthcareEntitiesDocumentResultWithDocumentDetectedLanguage
from ._models_py3 import HealthcareEntity
from ._models_py3 import HealthcareEntityLink
from ._models_py3 import HealthcareLROResult
from ._models_py3 import HealthcareLROTask
from ._models_py3 import HealthcareRelation
from ._models_py3 import HealthcareRelationEntity
from ._models_py3 import HealthcareResult
from ._models_py3 import HealthcareTaskParameters
from ._patch import InformationResolution
from ._models_py3 import InnerErrorModel
from ._models_py3 import InputError
from ._models_py3 import JobState
from ._models_py3 import KeyPhraseExtractionLROResult
from ._models_py3 import KeyPhraseLROTask
from ._models_py3 import KeyPhraseResult
from ._models_py3 import KeyPhraseResultDocumentsItem
from ._models_py3 import KeyPhraseTaskParameters
from ._models_py3 import KeyPhraseTaskResult
from ._models_py3 import KeyPhrasesDocumentResult
from ._models_py3 import LanguageDetectionAnalysisInput
from ._models_py3 import LanguageDetectionDocumentResult
from ._models_py3 import LanguageDetectionResult
from ._models_py3 import LanguageDetectionTaskParameters
from ._models_py3 import LanguageDetectionTaskResult
from ._models_py3 import LanguageInput
from ._patch import LengthResolution
from ._models_py3 import LinkedEntitiesDocumentResult
from ._models_py3 import LinkedEntity
from ._models_py3 import Match
from ._models_py3 import MultiLanguageAnalysisInput
from ._models_py3 import MultiLanguageInput
from ._patch import NumberResolution
from ._patch import NumericRangeResolution
from ._patch import OrdinalResolution
from ._models_py3 import PIIResultWithDetectedLanguage
from ._models_py3 import Pagination
from ._models_py3 import PiiEntitiesDocumentResult
from ._models_py3 import PiiEntityRecognitionLROResult
from ._models_py3 import PiiLROTask
from ._models_py3 import PiiResult
from ._models_py3 import PiiTaskParameters
from ._models_py3 import PiiTaskResult
from ._models_py3 import PreBuiltResult
from ._models_py3 import PreBuiltTaskParameters
from ._models_py3 import QuantityResolution
from ._models_py3 import RequestStatistics
from ._models_py3 import SentenceAssessment
from ._models_py3 import SentenceSentiment
from ._models_py3 import SentenceTarget
from ._models_py3 import SentimentAnalysisLROTask
from ._models_py3 import SentimentAnalysisTaskParameters
from ._models_py3 import SentimentConfidenceScorePerLabel
from ._models_py3 import SentimentDocumentResult
from ._models_py3 import SentimentLROResult
from ._models_py3 import SentimentResponse
from ._models_py3 import SentimentResponseDocumentsItem
from ._models_py3 import SentimentTaskResult
from ._patch import SpeedResolution
from ._models_py3 import SummaryContext
from ._models_py3 import TargetConfidenceScoreLabel
from ._models_py3 import TargetRelation
from ._models_py3 import TaskIdentifier
from ._models_py3 import TaskParameters
from ._models_py3 import TaskState
from ._models_py3 import TasksState
from ._models_py3 import TasksStateTasks
from ._patch import TemperatureResolution
from ._patch import TemporalSpanResolution
from ._patch import VolumeResolution
from ._patch import WeightResolution


from ._text_analytics_client_enums import AgeUnit
from ._text_analytics_client_enums import AnalyzeTextLROResultsKind
from ._text_analytics_client_enums import AnalyzeTextLROTaskKind
from ._text_analytics_client_enums import AnalyzeTextTaskKind
from ._text_analytics_client_enums import AnalyzeTextTaskResultsKind
from ._text_analytics_client_enums import AreaUnit
from ._text_analytics_client_enums import Association
from ._text_analytics_client_enums import Certainty
from ._text_analytics_client_enums import ClassificationType
from ._text_analytics_client_enums import Conditionality
from ._text_analytics_client_enums import DateTimeSubKind
from ._text_analytics_client_enums import DocumentSentimentValue
from ._text_analytics_client_enums import ErrorCode
from ._text_analytics_client_enums import ExtractiveSummarizationSortingCriteria
from ._text_analytics_client_enums import FhirVersion
from ._text_analytics_client_enums import HealthcareDocumentType
from ._text_analytics_client_enums import HealthcareEntityCategory
from ._text_analytics_client_enums import InformationUnit
from ._text_analytics_client_enums import InnerErrorCode
from ._text_analytics_client_enums import LengthUnit
from ._text_analytics_client_enums import NumberKind
from ._text_analytics_client_enums import PiiCategory
from ._text_analytics_client_enums import PiiDomain
from ._text_analytics_client_enums import RangeKind
from ._text_analytics_client_enums import RelationType
from ._text_analytics_client_enums import RelativeTo
from ._text_analytics_client_enums import ResolutionKind
from ._text_analytics_client_enums import ScriptKind
from ._text_analytics_client_enums import SentenceSentimentValue
from ._text_analytics_client_enums import SpeedUnit
from ._text_analytics_client_enums import State
from ._text_analytics_client_enums import StringIndexType
from ._text_analytics_client_enums import TargetRelationType
from ._text_analytics_client_enums import TemperatureUnit
from ._text_analytics_client_enums import TemporalModifier
from ._text_analytics_client_enums import TokenSentimentValue
from ._text_analytics_client_enums import VolumeUnit
from ._text_analytics_client_enums import WarningCodeValue
from ._text_analytics_client_enums import WeightUnit
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AbstractiveSummarizationLROResult',
    'AbstractiveSummarizationLROTask',
    'AbstractiveSummarizationResult',
    'AbstractiveSummarizationResultBase',
    'AbstractiveSummarizationTaskParameters',
    'AbstractiveSummarizationTaskParametersBase',
    'AbstractiveSummary',
    'AbstractiveSummaryDocumentResult',
    'AbstractiveSummaryDocumentResultWithDetectedLanguage',
    'AgeResolution',
    'AnalyzeTextDynamicClassificationInput',
    'AnalyzeTextEntityLinkingInput',
    'AnalyzeTextEntityRecognitionInput',
    'AnalyzeTextJobState',
    'AnalyzeTextJobStatistics',
    'AnalyzeTextJobsInput',
    'AnalyzeTextKeyPhraseExtractionInput',
    'AnalyzeTextLROResult',
    'AnalyzeTextLROTask',
    'AnalyzeTextLanguageDetectionInput',
    'AnalyzeTextPiiEntitiesRecognitionInput',
    'AnalyzeTextSentimentAnalysisInput',
    'AnalyzeTextTask',
    'AnalyzeTextTaskResult',
    'AreaResolution',
    'BaseResolution',
    'ClassificationDocumentResult',
    'ClassificationResult',
    'CurrencyResolution',
    'CustomEntitiesLROTask',
    'CustomEntitiesResult',
    'CustomEntitiesResultDocumentsItem',
    'CustomEntitiesTaskParameters',
    'CustomEntityRecognitionLROResult',
    'CustomLabelClassificationResult',
    'CustomLabelClassificationResultDocumentsItem',
    'CustomMultiLabelClassificationLROResult',
    'CustomMultiLabelClassificationLROTask',
    'CustomMultiLabelClassificationTaskParameters',
    'CustomResult',
    'CustomSingleLabelClassificationLROResult',
    'CustomSingleLabelClassificationLROTask',
    'CustomSingleLabelClassificationTaskParameters',
    'CustomTaskParameters',
    'DateTimeResolution',
    'DetectedLanguage',
    'DocumentDetectedLanguage',
    'DocumentDetectedLanguageString',
    'DocumentError',
    'DocumentRequestStatistics',
    'DocumentResult',
    'DocumentStatistics',
    'DocumentWarning',
    'DynamicClassificationDocumentResult',
    'DynamicClassificationResult',
    'DynamicClassificationResultDocumentsItem',
    'DynamicClassificationTaskParameters',
    'DynamicClassificationTaskResult',
    'EntitiesDocumentResult',
    'EntitiesLROTask',
    'EntitiesResult',
    'EntitiesResultWithDetectedLanguage',
    'EntitiesTaskParameters',
    'EntitiesTaskResult',
    'Entity',
    'EntityLinkingLROResult',
    'EntityLinkingLROTask',
    'EntityLinkingResult',
    'EntityLinkingResultWithDetectedLanguage',
    'EntityLinkingTaskParameters',
    'EntityLinkingTaskResult',
    'EntityRecognitionLROResult',
    'EntityWithResolution',
    'Error',
    'ErrorResponse',
    'ExtractedSummaryDocumentResult',
    'ExtractedSummaryDocumentResultWithDetectedLanguage',
    'ExtractedSummarySentence',
    'ExtractiveSummarizationLROResult',
    'ExtractiveSummarizationLROTask',
    'ExtractiveSummarizationResult',
    'ExtractiveSummarizationTaskParameters',
    'HealthcareAssertion',
    'HealthcareEntitiesDocumentResult',
    'HealthcareEntitiesDocumentResultWithDocumentDetectedLanguage',
    'HealthcareEntity',
    'HealthcareEntityLink',
    'HealthcareLROResult',
    'HealthcareLROTask',
    'HealthcareRelation',
    'HealthcareRelationEntity',
    'HealthcareResult',
    'HealthcareTaskParameters',
    'InformationResolution',
    'InnerErrorModel',
    'InputError',
    'JobState',
    'KeyPhraseExtractionLROResult',
    'KeyPhraseLROTask',
    'KeyPhraseResult',
    'KeyPhraseResultDocumentsItem',
    'KeyPhraseTaskParameters',
    'KeyPhraseTaskResult',
    'KeyPhrasesDocumentResult',
    'LanguageDetectionAnalysisInput',
    'LanguageDetectionDocumentResult',
    'LanguageDetectionResult',
    'LanguageDetectionTaskParameters',
    'LanguageDetectionTaskResult',
    'LanguageInput',
    'LengthResolution',
    'LinkedEntitiesDocumentResult',
    'LinkedEntity',
    'Match',
    'MultiLanguageAnalysisInput',
    'MultiLanguageInput',
    'NumberResolution',
    'NumericRangeResolution',
    'OrdinalResolution',
    'PIIResultWithDetectedLanguage',
    'Pagination',
    'PiiEntitiesDocumentResult',
    'PiiEntityRecognitionLROResult',
    'PiiLROTask',
    'PiiResult',
    'PiiTaskParameters',
    'PiiTaskResult',
    'PreBuiltResult',
    'PreBuiltTaskParameters',
    'QuantityResolution',
    'RequestStatistics',
    'SentenceAssessment',
    'SentenceSentiment',
    'SentenceTarget',
    'SentimentAnalysisLROTask',
    'SentimentAnalysisTaskParameters',
    'SentimentConfidenceScorePerLabel',
    'SentimentDocumentResult',
    'SentimentLROResult',
    'SentimentResponse',
    'SentimentResponseDocumentsItem',
    'SentimentTaskResult',
    'SpeedResolution',
    'SummaryContext',
    'TargetConfidenceScoreLabel',
    'TargetRelation',
    'TaskIdentifier',
    'TaskParameters',
    'TaskState',
    'TasksState',
    'TasksStateTasks',
    'TemperatureResolution',
    'TemporalSpanResolution',
    'VolumeResolution',
    'WeightResolution',
    'AgeUnit',
    'AnalyzeTextLROResultsKind',
    'AnalyzeTextLROTaskKind',
    'AnalyzeTextTaskKind',
    'AnalyzeTextTaskResultsKind',
    'AreaUnit',
    'Association',
    'Certainty',
    'ClassificationType',
    'Conditionality',
    'DateTimeSubKind',
    'DocumentSentimentValue',
    'ErrorCode',
    'ExtractiveSummarizationSortingCriteria',
    'FhirVersion',
    'HealthcareDocumentType',
    'HealthcareEntityCategory',
    'InformationUnit',
    'InnerErrorCode',
    'LengthUnit',
    'NumberKind',
    'PiiCategory',
    'PiiDomain',
    'RangeKind',
    'RelationType',
    'RelativeTo',
    'ResolutionKind',
    'ScriptKind',
    'SentenceSentimentValue',
    'SpeedUnit',
    'State',
    'StringIndexType',
    'TargetRelationType',
    'TemperatureUnit',
    'TemporalModifier',
    'TokenSentimentValue',
    'VolumeUnit',
    'WarningCodeValue',
    'WeightUnit',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()